# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 392
- HTTP: 153 alive / 68 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 193 alive / 158 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33174
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
