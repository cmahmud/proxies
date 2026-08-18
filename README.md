# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 242
- HTTP: 231 alive / 29 gold
- HTTPS: 144 alive / 8 gold
- SOCKS4: 229 alive / 136 gold
- SOCKS5: 187 alive / 69 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9666
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
