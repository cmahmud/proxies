# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 221
- HTTP: 194 alive / 27 gold
- HTTPS: 151 alive / 8 gold
- SOCKS4: 187 alive / 100 gold
- SOCKS5: 221 alive / 86 gold

## Historical pool

- Discovered: 91717
- Ever alive: 8648
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
