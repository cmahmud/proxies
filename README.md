# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 463
- HTTP: 128 alive / 97 gold
- HTTPS: 120 alive / 31 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 215 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46127
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
