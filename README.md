# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 422
- HTTP: 102 alive / 68 gold
- HTTPS: 35 alive / 18 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48963
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
