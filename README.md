# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 242
- HTTP: 456 alive / 24 gold
- HTTPS: 263 alive / 10 gold
- SOCKS4: 205 alive / 109 gold
- SOCKS5: 221 alive / 99 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10159
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
