# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 445
- HTTP: 402 alive / 95 gold
- HTTPS: 302 alive / 26 gold
- SOCKS4: 241 alive / 160 gold
- SOCKS5: 271 alive / 164 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28236
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
