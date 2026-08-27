# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 412
- HTTP: 98 alive / 65 gold
- HTTPS: 179 alive / 20 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40708
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
