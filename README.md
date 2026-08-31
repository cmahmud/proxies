# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 460
- HTTP: 147 alive / 93 gold
- HTTPS: 141 alive / 32 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 219 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46098
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
