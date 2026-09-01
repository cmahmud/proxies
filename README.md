# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 458
- HTTP: 120 alive / 85 gold
- HTTPS: 117 alive / 32 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46754
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
