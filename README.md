# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 476
- HTTP: 147 alive / 96 gold
- HTTPS: 119 alive / 41 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46953
- Ever gold: 1459

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
