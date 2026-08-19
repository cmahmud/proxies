# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 321
- HTTP: 330 alive / 49 gold
- HTTPS: 207 alive / 10 gold
- SOCKS4: 205 alive / 130 gold
- SOCKS5: 208 alive / 132 gold

## Historical pool

- Discovered: 128143
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
