# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 427
- HTTP: 336 alive / 93 gold
- HTTPS: 202 alive / 24 gold
- SOCKS4: 256 alive / 146 gold
- SOCKS5: 278 alive / 164 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28159
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
