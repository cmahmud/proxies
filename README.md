# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 473
- HTTP: 143 alive / 96 gold
- HTTPS: 125 alive / 41 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 205 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45049
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
