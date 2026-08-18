# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 246
- HTTP: 182 alive / 25 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 181 alive / 111 gold
- SOCKS5: 209 alive / 102 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
