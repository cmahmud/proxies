# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 414
- HTTP: 244 alive / 91 gold
- HTTPS: 186 alive / 21 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 247 alive / 153 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27569
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
