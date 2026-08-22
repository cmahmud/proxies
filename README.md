# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 435
- HTTP: 220 alive / 91 gold
- HTTPS: 153 alive / 27 gold
- SOCKS4: 212 alive / 153 gold
- SOCKS5: 241 alive / 164 gold

## Historical pool

- Discovered: 162754
- Ever alive: 31571
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
