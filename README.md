# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 467
- HTTP: 130 alive / 95 gold
- HTTPS: 123 alive / 37 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46880
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
