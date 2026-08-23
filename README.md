# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 377
- HTTP: 94 alive / 48 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
