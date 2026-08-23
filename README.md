# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 200
- HTTP: 162 alive / 42 gold
- HTTPS: 163 alive / 9 gold
- SOCKS4: 107 alive / 65 gold
- SOCKS5: 162 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32682
- Ever gold: 1196

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
