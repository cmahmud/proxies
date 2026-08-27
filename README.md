# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 403
- HTTP: 90 alive / 56 gold
- HTTPS: 101 alive / 16 gold
- SOCKS4: 181 alive / 167 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41527
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
