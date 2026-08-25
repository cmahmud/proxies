# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 420
- HTTP: 87 alive / 65 gold
- HTTPS: 86 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36081
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
