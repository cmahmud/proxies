# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 256
- HTTP: 394 alive / 32 gold
- HTTPS: 172 alive / 4 gold
- SOCKS4: 210 alive / 116 gold
- SOCKS5: 228 alive / 104 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11749
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
