# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 405
- HTTP: 173 alive / 83 gold
- HTTPS: 127 alive / 22 gold
- SOCKS4: 225 alive / 153 gold
- SOCKS5: 207 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25221
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
