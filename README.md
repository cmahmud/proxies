# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 426
- HTTP: 110 alive / 73 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48981
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
