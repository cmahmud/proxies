# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 416
- HTTP: 256 alive / 90 gold
- HTTPS: 174 alive / 27 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 246 alive / 155 gold

## Historical pool

- Discovered: 167123
- Ever alive: 32544
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
