# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 385
- HTTP: 191 alive / 64 gold
- HTTPS: 93 alive / 21 gold
- SOCKS4: 205 alive / 149 gold
- SOCKS5: 205 alive / 151 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25731
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
