# SyndProxy private pool

## Current pool

- Alive now: 1552
- Gold now: 595
- HTTP: 606 alive / 190 gold
- HTTPS: 488 alive / 92 gold
- SOCKS4: 216 alive / 144 gold
- SOCKS5: 242 alive / 169 gold

## Historical pool

- Discovered: 141228
- Ever alive: 23996
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
