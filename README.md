# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 455
- HTTP: 122 alive / 91 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49286
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
