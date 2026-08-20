# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 386
- HTTP: 187 alive / 74 gold
- HTTPS: 109 alive / 18 gold
- SOCKS4: 186 alive / 148 gold
- SOCKS5: 204 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25843
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
