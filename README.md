# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 403
- HTTP: 72 alive / 52 gold
- HTTPS: 59 alive / 18 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41678
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
