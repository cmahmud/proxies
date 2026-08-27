# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 411
- HTTP: 93 alive / 69 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41753
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
