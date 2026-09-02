# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 437
- HTTP: 104 alive / 78 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47673
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
