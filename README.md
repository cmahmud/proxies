# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 464
- HTTP: 152 alive / 96 gold
- HTTPS: 131 alive / 32 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 229 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46231
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
