# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 427
- HTTP: 105 alive / 70 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48990
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
