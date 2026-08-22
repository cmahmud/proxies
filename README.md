# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 349
- HTTP: 221 alive / 88 gold
- HTTPS: 129 alive / 28 gold
- SOCKS4: 172 alive / 107 gold
- SOCKS5: 227 alive / 126 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
