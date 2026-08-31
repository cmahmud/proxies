# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 459
- HTTP: 146 alive / 92 gold
- HTTPS: 147 alive / 33 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 225 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46088
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
