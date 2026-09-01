# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 425
- HTTP: 82 alive / 65 gold
- HTTPS: 75 alive / 28 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47154
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
