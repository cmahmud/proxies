# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 366
- HTTP: 91 alive / 65 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 159 alive / 137 gold
- SOCKS5: 163 alive / 148 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49559
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
