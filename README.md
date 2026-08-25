# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 422
- HTTP: 85 alive / 65 gold
- HTTPS: 84 alive / 22 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36082
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
