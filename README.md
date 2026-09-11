# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 425
- HTTP: 107 alive / 70 gold
- HTTPS: 40 alive / 21 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48990
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
