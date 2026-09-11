# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 453
- HTTP: 118 alive / 82 gold
- HTTPS: 52 alive / 32 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49226
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
