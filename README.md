# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 393
- HTTP: 387 alive / 84 gold
- HTTPS: 230 alive / 17 gold
- SOCKS4: 239 alive / 146 gold
- SOCKS5: 299 alive / 146 gold

## Historical pool

- Discovered: 134222
- Ever alive: 21769
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
