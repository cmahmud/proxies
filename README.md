# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 426
- HTTP: 109 alive / 73 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48987
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
