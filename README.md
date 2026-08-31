# SyndProxy validated proxy pool

## Current pool

- Alive now: 690
- Gold now: 463
- HTTP: 152 alive / 95 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 228 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46229
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
