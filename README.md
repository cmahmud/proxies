# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 469
- HTTP: 137 alive / 98 gold
- HTTPS: 68 alive / 37 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49369
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
