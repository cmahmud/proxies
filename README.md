# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 463
- HTTP: 143 alive / 95 gold
- HTTPS: 134 alive / 30 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 237 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46252
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
