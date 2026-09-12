# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 468
- HTTP: 118 alive / 91 gold
- HTTPS: 52 alive / 37 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49398
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
