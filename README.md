# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 411
- HTTP: 111 alive / 61 gold
- HTTPS: 166 alive / 18 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41003
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
