# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 416
- HTTP: 437 alive / 103 gold
- HTTPS: 316 alive / 28 gold
- SOCKS4: 247 alive / 152 gold
- SOCKS5: 242 alive / 133 gold

## Historical pool

- Discovered: 159263
- Ever alive: 30341
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
