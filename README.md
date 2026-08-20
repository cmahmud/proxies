# SyndProxy private pool

## Current pool

- Alive now: 1334
- Gold now: 561
- HTTP: 507 alive / 189 gold
- HTTPS: 375 alive / 93 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 230 alive / 132 gold

## Historical pool

- Discovered: 137899
- Ever alive: 22935
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
