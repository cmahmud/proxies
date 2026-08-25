# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 422
- HTTP: 86 alive / 65 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36081
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
