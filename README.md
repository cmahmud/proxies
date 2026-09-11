# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 428
- HTTP: 106 alive / 77 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48978
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
