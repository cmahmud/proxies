# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 426
- HTTP: 104 alive / 72 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48984
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
