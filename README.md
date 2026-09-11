# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 453
- HTTP: 117 alive / 84 gold
- HTTPS: 61 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49218
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
